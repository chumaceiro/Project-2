# Project 2 — Sales Record Analysis

Date Due: Apr 15, 2021 11:59 PM

# Description

You're an analyst at a multinational firm tasked with finding insights about specific questions asked by your supervisor. She has posed this task as a set of questions that you need to solve using the `sales_records.csv` file provided to you. 

# Column Descriptions

Check the PDF attached. 

# Questions

1. `compute_profit()` — The profit earned by the company and write it to the same csv file. 
    1. Formula: total_revenue - total_cost
2. `get_unique_country_per_region(region)` — Return the list of countries, and number of countries in a particular region

    ```python
    Output: 
    country_dict, number_dict

    country_list = {
    'region_1': [country_1, country_2],
    'region_3': [country_1, country_2],
    }

    number_dict = {
    'region_1': x,
    'region_2': y,
    }

     
    ```

3. `profit_by_country(country)` — Return the amount of profit made by the organisation in a particular country

    ```python
    Output:
    profit_dict 

    profit_dict = {
    'country_1': x,
    'country_2': y,
    }

    ```

4. `priority_by_region(region)` — Return a dictionary of the number of orders in each priority for a particular region

```python
Output: priority_dict
priority_dict = {
'L': x,
'M': y,
'H': z
} 
```

5. `item_type_unit_sold()` — Return a dictionary of the number of items sold for each item type

```python
Output: item_type_dict

item_dict = {
'item_type_1': x,
'item_type_2': y,
}

```

6. `item_shipped_within(days)` — Return a list of `order_id` where the difference between order date and shipped date is less than days, along with number of orders 

```python
Output: order_id_list, no_of_orders

order_id_list = ['order_id_1', 'order_id_2']
```

7. `country_revenue_item_type(country)` — Return the total amount of revenue generated for each item type in a country.  

```python
Output: country_revenue_dict

country_revenue_dict = {
		'country_1': {
			'item_type_1': x,
			'item_type_2': y
		},
		'country_2': {
			'item_type_1': x,
			'item_type_2': y
		},
		'country_3': {
			'item_type_1': x,
			'item_type_2': y
		}
}
```

8. `profit_between_days(day_1, day_2)` — Return the amount of profit made by the organisation for each item type between day_1, and day_2 (Use `order_date` for starting and end date)

```python
Output: item_revenue_dict 

item_revenue_dict = {
'item_type_1': x,
'item_type_2': y,
'item_type_3': z
}
```

9. `count_unique_item_types()` — Return the number of unique item_type present in the dataset. 

```python
Output: unique_items

unique_items = x (x --> int)
```

10. `top_5_profitable_items()` — Return top 5 order_id which generated most profit

```python
Output: top_5_orders

top_5_orders = ['order_id_1', 'order_id_2', 'order_id_3' ,'order_id_4']
```
