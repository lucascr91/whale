# pylint: disable=invalid-name,line-too-long
import re
import os
from glob import glob
import sys

import pandas as pd
from unidecode import unidecode
from tqdm import tqdm

from utils import create_table_and_upload_to_gcs


def get_caged_data(table_id: str, yearmonth: int) -> None:
    """
    Get CAGED data

    table_id: microdados_movimentacao | microdados_movimentacao_fora_prazo | microdados_movimentacao_excluida
    yearmonth: format YYYYMM
    """
    year = str(yearmonth)[:4]
    if int(year) not in [2020, 2021, 2022]:
        raise ValueError("Year must be 2020, 2021 or 2022")
    groups = {
        "microdados_movimentacao": "cagedmov",
        "microdados_movimentacao_fora_prazo": "cagedfor",
        "microdados_movimentacao_excluida": "cageddex",
    }

    group = groups[table_id]
    command = f"bash download.sh {group} {table_id} {yearmonth}"

    os.system(command)


def build_partitions(table_id: str) -> str:
    """
    build partitions from gtup files
    table_id: microdados_movimentacao | microdados_movimentacao_fora_prazo | microdados_movimentacao_excluida
    """
    input_files = glob(f"/tmp/caged/{table_id}/input/*txt")
    for filename in tqdm(input_files):
        df = pd.read_csv(filename, sep=";", dtype={"uf": str})
        date = re.search(r"\d+", filename).group()
        ano = date[:4]
        mes = int(date[-2:])

        df.columns = [unidecode(col) for col in df.columns]

        dict_uf = {
            "11": "RO",
            "12": "AC",
            "13": "AM",
            "14": "RR",
            "15": "PA",
            "16": "AP",
            "17": "TO",
            "21": "MA",
            "22": "PI",
            "23": "CE",
            "24": "RN",
            "25": "PB",
            "26": "PE",
            "27": "AL",
            "28": "SE",
            "29": "BA",
            "31": "MG",
            "32": "ES",
            "33": "RJ",
            "35": "SP",
            "41": "PR",
            "42": "SC",
            "43": "RS",
            "50": "MS",
            "51": "MT",
            "52": "GO",
            "53": "DF",
        }

        df["uf"] = df["uf"].map(dict_uf)

        for state in dict_uf.values():
            data = df[df["uf"] == state]
            data.drop(["competenciamov", "uf"], axis=1, inplace=True)
            data.to_csv(
                f"/tmp/caged/{table_id}/ano={ano}/mes={mes}/sigla_uf={state}/data.csv",
                index=False,
            )
            del data
        del df

    return f"/tmp/caged/{table_id}/"


def main():
    table_id = sys.argv[1]
    dataset_id = "br_me_caged"
    yearmonth = int(sys.argv[2])
    get_caged_data(table_id, yearmonth)
    filepath = build_partitions(table_id)
    create_table_and_upload_to_gcs(
            data_path=filepath,
            dataset_id=dataset_id,
            table_id=table_id,
            dump_mode="append",
        )

if __name__ == "__main__":
    main()
