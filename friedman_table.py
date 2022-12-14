"""
.
"""
from itertools import permutations

import numpy as np
import pandas as pd


class Friedman:
    """
    Object oriented implementation of the Friedman test and nemenyi test.
    """
    def __init__(self, blocks: int, treatments: dict[str, list]) -> None:
        self._blocks = blocks
        self._treatments = treatments
        self._frame = pd.DataFrame(
            self._treatments, index=list(range(1, self._blocks + 1)))

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
            raise ValueError(
                "can only compute friedman test for 3 dependant samples or more")

        # calculate average and std for given metric
        avg_metric = self._frame.mean()
        std_metric = self._frame.std()

        # create a ranking table
        self._ranks = self._rank(asc)
        # get averages for each algorithm
        avg = self._ranks.loc[~self._ranks.index.isin(
            ["Average", "Std"]), :].mean()
        # concatenate rank and metric table
        self._friedman_table = self._cat(self._ranks)
        # get average rank, metric and std
        self._friedman_table.loc["Average", :] = avg_metric
        self._friedman_table.loc["Std", :] = std_metric
        self._friedman_table.loc["Average rank", :] = avg

    def friedman_statistic(self) -> float:
        n = self._blocks
        k = len(self._treatments.keys())
        n1 = (k + 1) / 2
        n2 = n * np.sum((self._friedman_table.loc["Average rank", :] - n1)**2)
        n3 = np.sum(np.sum(((self._ranks - n1)**2).values)) / (n * (k - 1))
        return n2 / n3

    def critical_difference(self) -> float:
        """
        Description:
            Computes the critial distance of the nemenyi test.

        Returns:
            returns the critical distance
        """
        k: int = len(self._treatments.keys())
        N: int = self._blocks

        if k < 2:
            raise ValueError(
                "can only compute nemenyi for 3 samples or more")

        q_alpha = [1.960, 2.343, 2.569, 2.728,
                   2.850, 2.949, 3.031, 3.102, 3.164]

        return q_alpha[k - 1] * np.sqrt((k * (k + 1)) / (6 * N))

    def nemenyi(self) -> pd.Series:
        """
        Description:
            Computes nemenyi test

        Returns:
            pandas series with the treatments that display significant difference set as True and all others that fail to pass threshold to false.
        """

        average_row = self._friedman_table.loc["Average rank"]
        perm = permutations(average_row, 2)
        perm = [sorted(item) for item in perm]
        perm = list(set(map(tuple, perm)))
        diff = np.diff(perm)
        index = np.where(
            np.any(diff > self.critical_difference(), axis=1))[0][0]

        return average_row.isin(perm[index])

    @property
    def get_table(self) -> pd.DataFrame:
        """
        Description:
            Returns friedman table (ranks and values)

        Returns:
            pandas dataframe: Friedman table
        """
        return self._friedman_table

    @property
    def get_data(self) -> pd.DataFrame:
        """
        Description:
            Returns performance scores
        Returns:
            pandas dataframe: performance score
        """
        return self._frame

    @property
    def get_ranks(self) -> pd.DataFrame:
        """
        Description:
            Returns ranks
        Returns:
            pandas dataframe: ranks
        """
        return self._ranks
