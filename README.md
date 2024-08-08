# secret-santa

## Requirements
```python
pip install -r requirements.txt
```

## Usage
1. Ensure you have the data input `data.csv` in the folder
2. `python main.py` in the terminal
3. Collect your `results.tsv`, a tab-separated value file

### data.csv Format
| USERNAME | GROUP_RECV | FROM_GEO | GROUP_SEND | TO_GEO | ADDRESS |
| ---- | ---- | ---- | ---- | ---- | ---- |
| The person's name | The group(s) they want to receive | The country they are in | The group(s) they want to send | The countries thye want to send to | Their address |

**Country Codes**: `US`, `CA`