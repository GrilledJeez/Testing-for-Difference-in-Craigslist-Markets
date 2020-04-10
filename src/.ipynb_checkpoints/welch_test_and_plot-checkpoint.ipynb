{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import scipy.stats as stats\n",
    "import scipy as sp\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import math\n",
    "\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "import matplotlib.pylab as pylab\n",
    "%matplotlib inline\n",
    "plt.style.use('ggplot')\n",
    "\n",
    "\n",
    "def welch_test_and_plot(test_city, city_list):\n",
    "    for city in city_list:\n",
    "        print(\"{} vs {}\".format(test_city.iloc[0,5], city.iloc[0,5]))\n",
    "        test_statistic, p_value = np.round(stats.ttest_ind(test_city['price'], city['price']), 4)\n",
    "        ss1 = len(test_city['price'])\n",
    "        ss2 = len(city['price'])\n",
    "        deg_f = math.floor(\n",
    "            ((np.var(test_city['price'])/ss1 + np.var(city['price'])/ss2)**(2.00)) / \n",
    "            ((np.var(test_city['price'])/ss1)**(2)/(ss1 - 1) + (np.var(city['price'])/ss2)**(2)/(ss2 - 1))\n",
    "        )\n",
    "\n",
    "        x = np.linspace(-5, 5, num=400)\n",
    "        fig, ax = plt.subplots(1, figsize=(12, 4))\n",
    "        students = stats.t(deg_f)\n",
    "        ax.plot(x, students.pdf(x), linewidth=2, label=\"Degree of Freedom: {:2.0f}\"\n",
    "                .format(deg_f))\n",
    "        _ = ax.fill_between(x, students.pdf(x), where=(x >= abs(test_statistic)), color=\"red\",\n",
    "                alpha=0.25, label = \"P Value:\\\n",
    "                    {:2.4f}\".format(p_value))\n",
    "        _ = ax.fill_between(x, students.pdf(x), where=(x <= -(abs(test_statistic))), color=\"red\", \n",
    "                alpha=0.25)\n",
    "        ax.axvline(x=test_statistic, linewidth=4, color='r', label = \"Test Stat:\\\n",
    "                 {:2.4f}\".format(test_statistic), linestyle = '--')\n",
    "        ax.legend(bbox_to_anchor=(1,1), loc = 'upper left')\n",
    "        plt.xlabel('x', fontsize = 14, color = 'black')\n",
    "        plt.ylabel('Probability Density', fontsize = 14, color = 'black')\n",
    "        ax.set_title(\"{}-{} Welch Test Results\".format(test_city.iloc[1,5], city.iloc[1,5]), fontsize = 20, color = 'black')\n",
    "        plt.tight_layout()\n",
    "        plt.show()\n",
    "        \n",
    "if __name__ == __main__:\n",
    "    welch_test_and_plot()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
