import csv
from pathlib import Path
from typing import Union, List, Tuple, Optional


def ensure_parent_dir(path: str | Path) -> None:
    """
    Creates parent directories for the specified path if they don't exist.
    Args:
    path: Path to the file.
    """
    path_obj = Path(path)
    if path_obj.parent:
        path_obj.parent.mkdir(parents=True, exist_ok=True)


def write_csv(
    rows: List[Union[Tuple, List]],
    path: Union[str, Path],
    header: Optional[Tuple[str, ...]] = None,
) -> None:
    """
    Creates or rewrites a ',' delimited CSV file.
    If a header is provided, it is written as the first row.
    Checks that all rows in `rows` are the same length.
    Args:
        rows: List of tuples or lists representing the rows of data.
        path: Path to the file to write to.
        header: An optional tuple of rows representing the CSV header.
    Raises:
        ValueError: If not all rows in `rows` are the same length.
    """
    if not rows:
        # If there is no data, we write only the header, if there is one
        if header is not None:
            ensure_parent_dir(path)
            with open(path, "w", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(header)
        return

    # Проверка на одинаковую длину строк
    first_row_len = len(rows[0])
    if not all(len(row) == first_row_len for row in rows):
        raise ValueError("All data lines must be the same length.")

    # Если есть заголовок, проверяем его длину
    if header is not None and len(header) != first_row_len:
        raise ValueError(
            "The header length does not match the length of the data lines."
        )

    ensure_parent_dir(path)

    with open(path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        if header:
            writer.writerow(header)
        writer.writerows(rows)
