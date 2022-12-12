import pandas as pd
import numpy as np

class Friedman:
    def __init__(self,  blocks: int, treatments: dict[list]) -> None:
        self._blocks = blocks
        self._treatments = treatments
    
    def _create_table(self) -> pd.DataFrame:
        """
        Description:
            Dataframe with the columns equal to the treatment groups and the values for each column equal to the treatment results.

        Returns:
            Returns a dataframe.
        """
        return pd.DataFrame(self._treatments, index=[i for i in range(1, self._blocks + 1)]) 
    
    def _rank(self, frame: pd.DataFrame) -> pd.DataFrame:
        """
        Description:
            Ranks dataframe rows according to max value. Ranks assigned in ascending order from 1.

        Args:
            frame: Dataframe to rank.
            
        Returns:
            Returns dataframe with ranks.
        """
        return frame.rank(axis=1, method="max", ascending=False)
    
    def _cat(self, frame: pd.DataFrame, ranks: pd.DataFrame) -> pd.DataFrame:
        """
        Description:
            Concatenates treatment table with ranks table.

        Args:
            frame: Dataframe with treatments.
            ranks: Dataframe with ranks.
            
        Returns:
            Returns concatenated dataframe.
        """
        return frame.apply(lambda x: x.astype(str).str.cat("(" + ranks[x.name].astype(str) + ")", sep=" "))
    
    def table(self) -> pd.DataFrame:
        """
        Description:
            Creates a friedman table according to the main literature (12.8).

        Returns:
            Returns friedman table.
        """
        if len(self._treatments.keys()) < 3:
            raise ValueError("can only compute nemeyi for 3 dependant samples or more")
            
        # create data frame
        frame = self._create_table()

        # calculate average and std for given metric
        frame.loc["Average", :] = frame.mean()
        frame.loc["Std", :] = frame.std()
        
        # create a ranking table
        ranks = self._rank(frame)
        # get averages for each algorithm
        avg = ranks.loc[~ranks.index.isin(["Average", "Std"])].mean() 
        # concatenate rank and metric table
        friedman_table = self._cat(frame, ranks)
        # get average rank
        friedman_table.loc["Average rank"] = avg

        return friedman_table
    
    def nemenyi(self) -> float:
        """
        Description:
            computes the critial distance of the nemenyi test.

        Returns:
            returns the critical distance
        """
        k: int = len(self._treatments.keys())
        N: int = self._blocks

        if k < 3:
            raise ValueError("can only compute nemeyi for 3 dependant samples or more")

        q_alpha = [
            1.960, 2.343, 2.569, 
            2.728, 2.850, 2.949, 
            3.031, 3.102, 3.164]

        return q_alpha[k] * np.sqrt((k*(k+1)) / (6*N))