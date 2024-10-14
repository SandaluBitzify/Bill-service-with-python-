from flask import Flask, request, jsonify
import json
import win32print
from srilankan_kot import create_srilankan_kot_data
from mongolian_kot import create_mongolian_kot_data
from ws_kot import world_spice_kot_data
from bill import bill_data

app = Flask(__name__)

# Function to get printer names from config.json
def get_printer_names():
    with open('config.json', 'r') as file:
        config = json.load(file)
    return config

# Function to send raw data to a printer
def send_raw_data(printer_name, data):
    hPrinter = win32print.OpenPrinter(printer_name)
    try:
        hJob = win32print.StartDocPrinter(hPrinter, 1, ("ESC/POS Print Job", None, "RAW"))
        win32print.StartPagePrinter(hPrinter)
        win32print.WritePrinter(hPrinter, data.encode('utf-8'))
        win32print.EndPagePrinter(hPrinter)
        win32print.EndDocPrinter(hPrinter)
    finally:
        win32print.ClosePrinter(hPrinter)

@app.route('/print_kot', methods=['POST'])
def print_kot():
    data = request.json
    ##import pdb; pdb.set_trace()
    
    print(f"DEBUG: Received data: {data}") 
    
    command = data.get('command')
    stallId = data.get('stallId')
    store_type = data.get('store_type')
    
    printers = get_printer_names()
    used_printers = []

    command_with_text = ""
    # Sample data
    island_name = data.get('island_name')
    kot_bot_no = data.get('kot_bot_no')
    invoice_no = data.get('invoice_no')
    terminal = data.get('terminal') 
    cashier = data.get('cashier')
    order_no = data.get('order_no')
    date = data.get('date')
    time = data.get('time')
    card_no = data.get('card_no')
    user = data.get('user')
    table_no = data.get('table_no')
    items = data.get('items')
    gross_total = data.get('gross_total')
    discount = data.get('discount')
    subtotal = data.get('subtotal')
    vat = data.get('vat')
    total = data.get('total')
    
     # Generate the KOT layout
    #command_with_text = world_spice_kot_data(island_name, kot_bot_no, order_no, date, time, card_no, user, table_no, items, gross_total, discount, subtotal, vat, total)
    #command_with_text = create_srilankan_kot_data(island_name, kot_bot_no, order_no, date, time, card_no, user, items, gross_total, vat, total)
    
    #with open('kot_output.txt', 'w') as f:
    #    f.write(command_with_text) 
    #print(f"DEBUG: Received command: {command}, StallId: {stallId}, Order No: {order_no}, Card No: {card_no}, User: {user}, Items: {items}")  # Debugging line

    if command == "KOT":
        if stallId == "Sri Lanka":
            command_with_text = create_srilankan_kot_data(island_name, kot_bot_no, order_no, date, time, card_no, user, items, gross_total, vat, total)
            send_raw_data(printers["srilanka_printer"], command_with_text)
            used_printers.append(printers["srilanka_printer"])
            if store_type == "WSBEVERAGE":
                send_raw_data(printers["beverage_printer"], command_with_text)
                used_printers.append(printers["beverage_printer"])
        elif stallId == "Mongolian":
            command_with_text = create_mongolian_kot_data(island_name, kot_bot_no, order_no, date, time, card_no, user, items, gross_total, vat, total)
            send_raw_data(printers["mongolian_printer"], command_with_text)
            used_printers.append(printers["mongolian_printer"])
            if store_type == "WSBEVERAGE":
                send_raw_data(printers["beverage_printer"], command_with_text)
                used_printers.append(printers["beverage_printer"])
        elif stallId == "Bar":
            if store_type == "MAINKITCHEN":
                send_raw_data(printers["kitchen_printer"], command_with_text)
                used_printers.append(printers["kitchen_printer"])
            send_raw_data(printers["bar_printer"], command_with_text)
            used_printers.append(printers["bar_printer"])
        elif stallId == "WSCHINESE":
            command_with_text = world_spice_kot_data(island_name, kot_bot_no, order_no, date, time, card_no, user, items, gross_total, vat, total)
            send_raw_data(printers["chinese_printer"], command_with_text)
            used_printers.append(printers["chinese_printer"])
        elif stallId == "WSINDIAN":
            command_with_text = world_spice_kot_data(island_name, kot_bot_no, order_no, date, time, card_no, user, items, gross_total, vat, total)
            send_raw_data(printers["indian_printer"], command_with_text)
            used_printers.append(printers["indian_printer"])
        elif stallId == "WSITALIAN":
            command_with_text = world_spice_kot_data(island_name, kot_bot_no, order_no, date, time, card_no, user, items, gross_total, vat, total)
            send_raw_data(printers["italian_printer"], command_with_text)
            used_printers.append(printers["italian_printer"])
        elif stallId == "WSTHAI":
            command_with_text = world_spice_kot_data(island_name, kot_bot_no, order_no, date, time, card_no, user, items, gross_total, vat, total)
            send_raw_data(printers["thai_printer"], command_with_text)
            used_printers.append(printers["thai_printer"])
        elif stallId == "WSSNKDST":
            command_with_text = world_spice_kot_data(island_name, kot_bot_no, order_no, date, time, card_no, user, items, gross_total, vat, total)
            send_raw_data(printers["snkdst_printer"], command_with_text)
            used_printers.append(printers["snkdst_printer"])
        elif stallId == "WSBEVERAGE":
            command_with_text = world_spice_kot_data(island_name, kot_bot_no, order_no, date, time, card_no, user, items, gross_total, vat, total)
            send_raw_data(printers["beverage_printer"], command_with_text)
            used_printers.append(printers["beverage_printer"])
   
        """    
        elif stallId == "WSINDIAN":
            send_raw_data("indian_printer", command_with_text)
            used_printers.append("indian_printer")
        elif stallId == "WSITALIAN":
            send_raw_data("italian_printer", command_with_text)
            used_printers.append("italian_printer")
        elif stallId == "WSTHAI":
            send_raw_data("thai_printer", command_with_text)
            used_printers.append("thai_printer")
        elif stallId == "WSSNKDST":
            send_raw_data("snkdst_printer", command_with_text)
            used_printers.append("snkdst_printer")
        elif stallId == "WSBEVERAGE":
            send_raw_data("bevarage_printer", command_with_text)
            used_printers.append("bevarage_printer")
        elif stallId == "KCCCAKE":
            send_raw_data("cakebaker_printer", command_with_text)
            used_printers.append("cakebaker_printer")
        elif stallId == "KCCFRESH":
            send_raw_data("fresh_printer", command_with_text)
            used_printers.append("fresh_printer")
        """ 
    if command == "BILL":
        stallId == "cashier1" 
        command_with_text = bill_data(island_name, invoice_no, terminal, cashier, date, time, table_no, items, gross_total, discount, subtotal, vat, total)
        send_raw_data(printers["cashier1_printer"], command_with_text)
        used_printers.append(printers["cashier1_printer"])     
        
    #return jsonify({"status": "success", "used_printers": used_printers}), 200
    # If command_with_text is still an empty string, raise an error or log it
    if not command_with_text:
        return jsonify({"error": "No valid KOT layout generated"}), 400

    # Save the output to a file for debugging
    with open('kot_output.txt', 'w') as f:
        f.write(command_with_text) 
        
    return jsonify({"status": "success", "used_printers": used_printers}), 200

if __name__ == '__main__':
    app.run(debug=True)
