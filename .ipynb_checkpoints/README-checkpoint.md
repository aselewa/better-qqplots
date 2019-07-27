## Better quantile-quantile plots in Python

#### `qqplot_unif()`

```
from scipy import stats
y_uniform = stats.uniform.rvs(size=1000)
qqplot_unif(y_uniform)
```

<img src=img/qqplot_uniform.png width="400" height="400" />


```
y_normal = stats.norm.rvs(loc=5,scale=2,size=1000)
qqplot_norm(y_normal)
```

<img src=img/qqplot_normal.png width="400" height="400" />