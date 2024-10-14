"""
def world_spice_kot_data(island_name, kot_bot_no, order_no, date, time, user, table_no, card_no,  items, gross_total, discount, subtotal, vat, total):
    esc_pos_data = ""
    esc_pos_data += "\x1b\x40"  # ESC @ Initialize
    esc_pos_data += "\x1b\x61\x01"  # Center alignment
    esc_pos_data += "               KANDY CITY CENTRE \n"
    esc_pos_data += "               #05, Dalada Veediya\n"
    esc_pos_data += "                 Kandy, Sri Lanka\n"
    esc_pos_data += "                T: +94 71 6 555555\n"
    esc_pos_data += "                F: +94 81 2 225792\n"
    esc_pos_data += "           E: dining.kandycitycentre.lk\n"
    esc_pos_data += "                VAT NO: 114215570-7000\n\n"
    esc_pos_data += "---------------------------------------------\n\n"
    esc_pos_data += f"Island Name: {island_name}\n"
    esc_pos_data += f"KOT/BOT No:  {kot_bot_no}\n\n"
    esc_pos_data += "---------------------------------------------\n"
    esc_pos_data += f"Invoice No:         {order_no}\n"
    esc_pos_data += f"Date:               {date}\n"
    esc_pos_data += f"Time:               {time}\n"
    esc_pos_data += f"Card No:            {card_no}\n"
    esc_pos_data += f"User:               {user}\n"  
    esc_pos_data += f"Table No:           {table_no}\n"
    esc_pos_data += "-----------------------------------------------\n"
    esc_pos_data += "ITEM                              QTY    PRICE       AMOUNT\n"
    esc_pos_data += "-----------------------------------------------------------\n"
    
    for item in items:
        esc_pos_data += f"{item['name']: <30} {item['quantity']: >3} {item['price']: >10.2f} {item['amount']: >10.2f}\n"

    esc_pos_data += "-----------------------------------------------------------\n"
    esc_pos_data += f"Gross Total:                                                        {gross_total:.2f}\n"
    esc_pos_data += f"Less Discounts:                                                  {discount:.2f}\n"
    esc_pos_data += f"Sub Total:                                                          {subtotal:.2f}\n"
    esc_pos_data += f"VAT:                                                                     {vat:.2f}\n"
    esc_pos_data += "-----------------------------------------------------------\n"
    esc_pos_data += f"Total:                                                               {total:.2f}\n\n"
    esc_pos_data += "                ALL ABOVE PRICES ARE SUBJECT TO TAXES \n"
    esc_pos_data += "\x1b\x64\x03"  # Feed 3 lines
    esc_pos_data += "\x1b\x69"      # Full cut
    return esc_pos_data
"""  
def world_spice_kot_data(island_name, kot_bot_no, order_no, date, time, card_no, user, items, gross_total, vat, total):
    esc_pos_data = ""
    esc_pos_data += "\x1b\x40"  # ESC @ Initialize
    #esc_pos_data += "\x1b\x61\x01"  # Center alignment
    esc_pos_data += "  KANDY CITY CENTRE \n"
    esc_pos_data += "       WORLDSPICE\n\n"
    esc_pos_data += f"    Island Name: {island_name}\n"
    esc_pos_data += f"      KOT/BOT No:  {kot_bot_no}\n"
    esc_pos_data +=        f"Order No:      {order_no}\n"
    esc_pos_data += f"Date:               {date}\n"
    esc_pos_data += f"Time:               {time}\n"
    esc_pos_data += f"Card No:            {card_no}\n"
    esc_pos_data += f"User:               {user}\n"   
    esc_pos_data += "-----------------------------------------\n"
    esc_pos_data += "ITEM          QTY      PRICE     AMOUNT\n"
    esc_pos_data += "-----------------------------------------\n"
    
    for item in items:
        esc_pos_data += f"{item['name']: <13} {item['quantity']: >3} {item['price']: >10.2f} {item['amount']: >10.2f}\n"

    esc_pos_data += "-----------------------------------------\n"
    esc_pos_data += f"Gross Total:                 {gross_total: >10.2f}\n"
    esc_pos_data += f"VAT:                         {vat: >10.2f}\n"
    esc_pos_data += f"Total:                       {total: >10.2f}\n\n"
    esc_pos_data += " ALL ABOVE PRICES ARE SUBJECT TO TAXES \n"
    esc_pos_data += "\x1b\x64\x07"  # Feed 3 lines
    esc_pos_data += "\x1b\x69"      # Full cut
    return esc_pos_data