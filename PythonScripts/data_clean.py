# Helper script for functions that may be used across 2 or more notebooks

import pandas as pd
from pathlib import Path

# List of columns to drop. Columns are not used in this project. Used in NumPiecesRating and IPRatings
def drop_columns(df: pd.DataFrame) -> pd.DataFrame:
    drop_list = [
             'numberVariant',
                'released',
                'category',
                'bricksetURL',
                'reviewCount',
                'packagingType',
                'availability',
                'instructionsCount',
                'additionalImageCount',
                'lastUpdated',
                'image.thumbnailURL',
                'image.imageURL',
                'collections.ownedBy',
                'collections.wantedBy',
                'dimensions.height',
                'dimensions.width',
                'dimensions.depth',
                'LEGOCom.US.retailPrice',
                'LEGOCom.US.dateFirstAvailable',
                'LEGOCom.US.dateLastAvailable',
                'LEGOCom.UK.retailPrice',
                'LEGOCom.UK.dateFirstAvailable',
                'LEGOCom.UK.dateLastAvailable',
                'LEGOCom.CA.retailPrice',
                'LEGOCom.CA.dateFirstAvailable',
                'LEGOCom.CA.dateLastAvailable',
                'dimensions.weight',
                'barcode.EAN',
                'barcode.UPC',
                'minifigs',
                'LEGOCom.DE.retailPrice',
                'LEGOCom.DE.dateFirstAvailable',
                'LEGOCom.DE.dateLastAvailable'
                ]
    df.drop(columns=drop_list, inplace=True)

# Write a file to the CSV folder
def csv_path(file: str):
   parent_path = Path.cwd().absolute()
   csv_folder = Path('CSVs')
   large_path = Path.joinpath(parent_path,csv_folder,file).absolute()
   return large_path


if __name__ == "__main__":
    main()      
