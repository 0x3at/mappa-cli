import pandas as pd
import click

class FileHandler:
    def __init__(self, file_path):
        self.DataFrame = self._parse_datatable_to_df(file_path)
        self.OutputDataframe = self.DataFrame
        self.OutputPath = file_path+".mapped.csv"
        self.headers = self._extract_headers()
        self.rename_dict = self._build_rename_dict()

    def trigger_rename(self):
        self._rename_dataframe()

    def trigger_remap(self, new_order):
        self._remap_dataframe(new_order)

    def trigger_strip(self, columns):
        self._drop_columns(columns)
    
    def trigger_lowercase(self):
        self._lowercase_all_headers()

    def save_df_to_csv(self):
        click.echo(f"Saving to {self.OutputPath}")
        self.OutputDataframe.to_csv(self.OutputPath, index=False)
        click.echo("Saved successfully")

    def _parse_datatable_to_df(self, file_path):
        if file_path.endswith(".csv"):
            dataframe = pd.read_csv(file_path, engine="pyarrow")
        elif file_path.endswith(".xlsx"):
            dataframe = pd.read_excel(file_path, engine="openpyxl")
        return dataframe
    
    def _extract_headers(self):
        return self.DataFrame.columns.tolist()
    
    def _build_rename_dict(self):
        rename_dict = {}
        for header in self.headers:
            rename_dict[header] = header
        return rename_dict
    
    def _rename_dataframe(self):
        click.echo("Renaming headers")
        self.OutputDataframe = self.DataFrame.rename(columns=self.rename_dict, inplace=False)
        click.echo("Headers renamed successfully")

    def _remap_dataframe(self, new_order):
        click.echo("Remapping headers")
        self.OutputDataframe = self.DataFrame[new_order]
        click.echo("Headers remapped successfully")
    
    def _drop_columns(self, columns):
        click.echo("Dropping columns")
        self.OutputDataframe = self.DataFrame.drop(columns=columns)
        click.echo("Columns dropped successfully")

    def _lowercase_all_headers(self):
        click.echo("Setting headers to lowercase")
        self.OutputDataframe.columns = [header.lower() for header in self.headers]
        click.echo("Headers set to lowercase successfully")