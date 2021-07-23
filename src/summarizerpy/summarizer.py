import pandas as pd
from typing import (
    Any,
    Optional,
)

class Summarizer:
    def __init__(self, output : int = 0, out : str = None, output_type : str = None) -> None:
        self._output = output
        self._out = out
        self._output_type = output_type
        self._report = []
        self._validate_parameters()

    def _validate_parameters(self) -> None:
        if self._output not in [0,1]:
            raise ValueError("Error output choice")
        if self._output == 1:
            if self._out is None:
                raise ValueError("Error file name")
            if self._output_type not in ['markdown', 'xlsx', 'html']:
                raise ValueError("Error file type")

    def _summarize(self, df: pd.DataFrame) -> None:        
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Not Pandas DataFrame")

        for col in df.columns:
            self._report.append(df[col].describe())
        self._report = pd.concat(self._report, axis=1)

    def save_report(self, df: pd.DataFrame) -> Optional[str]:
        self._summarize(df)
        if(self._output == 0):
            return self._report.to_string()

        try:
            file = './' + self._out + '.' + self._output_type
            if self._output_type == 'xlsx':
                self._report.to_excel(file)
            elif self._output_type == 'html':
                self._report.to_html(file)
            elif self._output_type == 'markdown':
                self._report.to_markdown(file)
            print("File: " + file + ' saved')
        except Exception as e:
            raise ValueError("Error writing report")

