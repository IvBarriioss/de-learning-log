import polars as pl


def main():
    df = pl.DataFrame(
        {
            "tema": ["git", "uv", "polars"],
            "horas": [2, 1, 3],
        }
    )
    print(df)
    print(df.select(pl.col("horas").sum().alias("horas_totales")))


if __name__ == "__main__":
    main()
