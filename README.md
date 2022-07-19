# trevorfrench

trevorfrench does not currently have any dependencies.

## :writing_hand: Author

Trevor French <https://trevorfrench.com>

## :arrow_double_down: Installation

```python
!pip install trevorfrench --upgrade
```

## Functions: 

stats.one_way_anova

### stats.one_way_anova(*args)
- *args: lists containing samples to analyze
```python
from trevorfrench import stats as stats

list_1 = [6.9, 5.4, 5.8, 4.6, 4.0]
list_2 = [8.3, 6.8, 7.8, 9.2, 6.5]
list_3 = [8.0, 10.5, 8.1, 6.9, 9.3]

anova_table = stats.one_way_anova(list_1, list_2, list_3)
print(anova_table)

#RETURNS:

# {
#     'SST': 45.349333333333306
#     , 'SSE': 17.452000000000005
#     , 'SSR': 27.897333333333304
#     , 'df_treatment': 2
#     , 'df_error': 12
#     , 'df_total': 14
#     , 'MST': 13.948666666666652
#     , 'MSE': 1.4543333333333337
#     , 'F': 9.591107036442802
# }
```

## ACTION LIST
- Continue adding statistical methods
- Update README to have emojis instead of shortcuts and push to PyPi again