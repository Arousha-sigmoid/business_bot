rel_dataset_prompt = """
Below the query is given in triple backticks. Analyse the query and based on the below description for each dataset file, return a list of filenames which can be used to answer the query.
If the given query cannot be answered with any dataset files, then output ["None"]
Output format: 
```
['filename1','filename2',...] or ["None"]
```

Query:
```
{query}
```

File Name: "cross_transfers_data.csv"
The dataset "cross_transfers_power_bi_updated.csv" documents the transfer of materials between various plants, capturing essential details of each transfer event. Each row represents an individual transfer, including data on the material identifier, the sending and receiving plants, and product-specific information. Key columns include the material code, sending and receiving plant identifiers, product group, material document number, and booking date. Additionally, the dataset records the number of packages, master cartons, and pallets involved in each transfer, along with details of the sending and receiving warehouses. Cost-related data, such as proportional transfer costs, and classification codes for the materials, are also included to provide a comprehensive overview of the transfer events.

File Name: "inbound_primary_shipment.csv"
The "inbound_primary_shipment.csv" dataset offers a detailed record of primary shipments received by a plant. Each row details an individual shipment transaction, including logistics, financials, and classification information. Notable columns include the RSKU (Stock Keeping Unit), receiving plant code, location within the plant, and movement type. The dataset also captures the sending plant code, material document number, position within the shipment document, and booking date. Quantitative data includes the quantity received, base unit of measure, alternate unit of measure, corrected quantity if adjustments were made, and the number of pallets. Additionally, it records the total cost of the shipment, delivery note number, and various classifications such as ABC and XYZ classifications, which help in analyzing consumption value and demand variability.

File Name: "material_cost_month_level_data.csv"
The dataset "Material_DC_month_level_cost_data_updated.csv" provides monthly cost and logistics data at the material and distribution center (DC) level. Each row includes information on the number of inbound, inventory, and outbound pallets, as well as cross-transfer pallets. Cost data encompasses inbound and outbound transportation costs, handling costs, inventory costs, inter-warehouse transfer costs, and administrative costs. The dataset also includes columns for product type classifications, SKU (Stock Keeping Unit), material identifiers, and various classifications like ABC and XYZ, which help in understanding inventory value and demand variability. This dataset is crucial for analyzing and optimizing supply chain operations and cost management.

File Name: "outbound_data.csv"
The "outbound_data.csv" dataset captures detailed information on outbound logistics and deliveries. Each row represents a unique delivery event, documenting specifics such as delivery note numbers, transportation routes, customer details, and associated costs. Key columns include the distance traveled, tour number, postal code of the delivery destination, listing date, delivery area code, weight metrics, total pallets, and total volume shipped. The dataset also records financial details such as toll costs, administrative costs, and total delivery costs. Additional columns include mapping identifiers, year of the record, service levels, and geographical data like destination postal code, latitude, and longitude, providing a comprehensive view of outbound delivery operations.


"""