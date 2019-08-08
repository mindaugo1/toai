from typing import Optional, List


class DataParams:
    def __init__(
        self,
        target_col: str,
        cat_cols: Optional[List[str]] = None,
        cont_cols: Optional[List[str]] = None,
        text_cols: Optional[List[str]] = None,
    ):
        self.target_col = target_col
        self.cat_cols = cat_cols or []
        self.cont_cols = cont_cols or []
        self.text_cols = text_cols or []
        self.feature_cols = self.cat_cols + self.cont_cols
