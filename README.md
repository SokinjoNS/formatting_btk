# formatting_btk module for data formatting

This utility module, named `formatting`, provides essential functions for formatting numerical data and generating standardized chart URLs for cryptocurrency market data. 

Designed to enhance readability and consistency across crypto-related projects, it's particularly useful for scripts interfacing with Binance data and sending alerts through Telegram.

## FEATURES

- `format_number`: Formats large numerical values into a readable format with thousands separators.
- `generate_chart_url`: Generates URLs for viewing cryptocurrency charts on TradingView, supporting multiple platforms.

## USAGE

Import the module into your Python scripts to utilize its functions for data presentation enhancements:

```python
from formatting import format_number, generate_chart_url

EXAMPLE:
volume = 1234567.89
formatted_volume = format_number(volume)
print(formatted_volume)  # Outputs: 1,234,567.89
```

## CONTRIBUTIONS

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or create a pull request.

## LICENSE

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

