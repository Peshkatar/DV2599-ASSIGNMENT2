import numpy as np
import pandas as pd

class Friedman:
    def __init__(self, blocks: int, treatments: dict[str, list]) -> None:
        self._blocks = blocks
        self._treatments = treatments
        self._frame = pd.DataFrame(self._treatments, index=list(range(1, self._blocks + 1)))

    def _rank(self, asc: bool) -> pd.DataFrame:
        """
        Description:
            Ranks dataframe rows according to max value. Ranks assigned in ascending order from 1.

        Args:
            frame: Dataframe to rank.
            asc: whether to rank from lowest to highest or other way

        Returns:
            Returns dataframe with ranks.
        """
        return self._frame.rank(axis=1, method="max", ascending=asc).astype(np.int8)

    def _cat(self, ranks: pd.DataFrame) -> pd.DataFrame:
        """
        Description:
            Concatenates treatment table with ranks table.

        Args:
            frame: Dataframe with treatments.
            ranks: Dataframe with ranks.

        Returns:
            Returns concatenated dataframe.
        """
        # join kanske?
        return self._frame.apply(
            lambda x: x.astype(str).str.cat(
                "(" + ranks[x.name].astype(str) + ")", sep=" "
            )
        )

    def create_table(self, *, asc=False) -> None:
        """
        Description:
            Creates a friedman table according to the main literature (12.8).
        """
        if len(self._treatments.keys()) < 3:
            raise ValueError("can only compute friedman test for 3 dependant samples or more")   

        # calculate average and std for given metric
        avg_metric = self._frame.mean()
        std_metric = self._frame.std()
        
        # create a ranking table
        self._ranks = self._rank(asc)
        # get averages for each algorithm
        avg = self._ranks.loc[~self._ranks.index.isin(["Average", "Std"]), :].mean()
        # concatenate rank and metric table
        self._friedman_table = self._cat(self._ranks)
        # get average rank, metric and std
        self._friedman_table.loc["Average", :] = avg_metric
        self._friedman_table.loc["Std", :] = std_metric
        self._friedman_table.loc["Average rank", :] = avg

    @property
    def get_frame(self) -> pd.DataFrame:
        return self._friedman_table

    def friedman_statistic(self) -> float:
        n = self._blocks
        k = len(self._treatments.keys())
        n1 = (k + 1) / 2
        n2 = n * sum((self._friedman_table.loc["Average rank", :] - n1)**2)
        n3 = sum(((self._ranks - n1)**2).values).sum() / (n * (k - 1))
        return n2 / n3   
    
    def test(self) -> str:
        return "Null hypothesis rejected" if self.friedman_statistic() > 7.8 else "Null hypothesis not rejected"

    def critical_difference(self) -> float:
        """
        Description:
            computes the critial distance of the nemenyi test.

        Returns:
            returns the critical distance
        """
        k: int = len(self._treatments.keys())
        N: int = self._blocks

        if k < 2:
            raise ValueError("can only compute nemenyi for 3 dependant samples or more")

        q_alpha = [1.960, 2.343, 2.569, 2.728, 2.850, 2.949, 3.031, 3.102, 3.164]

        return q_alpha[k - 1] * np.sqrt((k * (k + 1)) / (6 * N))

    def nemenyi_test(self) -> str:
        x1 = self._friedman_table.loc["Average rank", "Support Vector Machine"] - self._friedman_table.loc["Average rank", "AdaBoost"]
        x2 = self._friedman_table.get_frame.loc["Average rank", "Support Vector Machine"] - self._friedman_table.get_frame.loc["Average rank", "Random Forest"]
        x3 = self._friedman_table.get_frame.loc["Average rank", "AdaBoost"] - self._friedman_table.get_frame.loc["Average rank", "Random Forest"]
        #perm = permutations(
            [self._friedman_table.loc["Average rank", "Support Vector Machine"],
             self._friedman_table.get_frame.loc["Average rank", "AdaBoost"],
             self._friedman_table.get_frame.loc["Average rank", "Random Forest"]])
        #sub = map(permuations, )
        return any([x1, x2, x3] > self.critical_difference())
    
            
        
  
  
