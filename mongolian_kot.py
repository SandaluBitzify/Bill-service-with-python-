def create_mongolian_kot_data(island_name, kot_bot_no, order_no, date, time, card_no, user, items, gross_total, vat, total):
    esc_pos_data = ""
    esc_pos_data += "\x1b\x40"  # ESC @ Initialize
    esc_pos_data += "\x1b\x61\x01"  # Center alignment
    esc_pos_data += "MONGOLIAN STALL\n"
    esc_pos_data += "\x1b\x61\x00"  # Left alignment
    esc_pos_data += f"Island Name: {island_name}\n"
    esc_pos_data += f"KOT/BOT No: {kot_bot_no}\n\n"
    esc_pos_data += f"Order No: {order_no}\n\n"
    esc_pos_data += f"Date: {date}  Time: {time}\n"
    esc_pos_data += f"Card No: {card_no}\n"
    esc_pos_data += f"User: {user}\n\n"
    esc_pos_data += "Item Name                     Amount\n"
    esc_pos_data += "----------------------------------------\n"
    for item in items:
        esc_pos_data += f"{item['name']}                     {item['price']:.2f}\n"
        esc_pos_data += f"({item['quantity']:.2f} X {item['price']:.2f})\n\n"
    esc_pos_data += f"GROSS TOTAL                   {gross_total:.2f}\n"
    esc_pos_data += f"VAT                           {vat:.2f}\n"
    esc_pos_data += "----------------------------------------\n"
    esc_pos_data += f"TOTAL                         {total:.2f}\n\n"
    esc_pos_data += "\x1b\x61\x01"  # Center alignment
    esc_pos_data += "ALL ABOVE PRICES ARE\n"
    esc_pos_data += "SUBJECT TO TAXES\n"
    esc_pos_data += "\x1b\x64\x03"  # Feed 3 lines
    esc_pos_data += "\x1b\x69"      # Full cut
    return esc_pos_data
