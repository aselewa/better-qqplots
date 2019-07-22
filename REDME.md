## Better quantile-quantile plots in Python

#### `qqplot_unif()`

```
from scipy import stats
y = stats.uniform.rvs(size=1000)
qqplot_unif(y)
```

<img src=img/qqplot_uniform.png width="500" height="400" />
