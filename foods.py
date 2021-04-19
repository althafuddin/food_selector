import random

Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
Fruits = ["Strawberry", "Avocado", "Oranges", "Blue Berries", "Black Berries", "Peaches",
 "Pears", "Apple", "Banana", "Kiwi"]
Veggies = ["Sweet Potato", "Green Beans", "Zucchini", "Cucumber", "Spinach", "Broccoli", 
"Carrots", "Cauliflower", "Brussels Sprouts", "Okra", "Chinese Okra", "Peppers"]
Proteins = ["Eggs", "Paneer", "Chicken", "Fish", "Mutton", "Yogurt"]
Grains = ["Rice", "Quinoa", "Oats", "Ragi"] 
Recipe = ["Pureed", "Balls of"]
Cook = ["Baked", "Roasted", "Steamed"]
##########


def Breakfast(veggielist, fruitlists):
    veggie = random.choices(veggielist)
    fruit = random.choices(fruitlists)
    x = veggie + fruit
    return x 

def Lunch(protienlist, grainslist):
    protein = random.choices(Proteins)
    grain = random.choices(Grains)
    x = protein + grain
    return x 

def Html_formater():
    strTable = """
    <style type="text/css">
        .tg  {border-collapse:collapse;border-color:#aaa;border-spacing:0;}
        .tg td{background-color:#fff;border-color:#aaa;border-style:solid;border-width:1px;color:#333;
        font-family:Arial, sans-serif;font-size:24px;overflow:hidden;padding:10px 5px;word-break:normal;}
        .tg th{background-color:#f38630;border-color:#aaa;border-style:solid;border-width:1px;color:#fff;
        font-family:Arial, sans-serif;font-size:24px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
        .tg .tg-0lax{text-align:left;vertical-align:top}
        </style>
        <table class="tg">
        <thead>
        <tr>
            <th class="tg-fymr"><b>Day</b></th>
            <th class="tg-fymr"><b>Fruit</b></th>
            <th class="tg-fymr"><b>Veggie</b></th>
            <th class="tg-fymr"><b>Protein</b></th>
            <th class="tg-fymr"><b>Grain</b></th>
            <th class="tg-fymr"><b>Suggested Recipes</b></th>
        </tr>
        </thead>
        <tbody>
    """
    Html_Str = ""
    for i in range(7):
        strRW = f"<tr><td class=\"tg-fymr\"><b>{Days[i]}</b></td>"
        strRW += f"<td class=\"tg-0lax\">{bf_items[i][0]}</td>"
        strRW += f"<td class=\"tg-0lax\">{bf_items[i][1]}</td>"
        strRW += f"<td class=\"tg-0lax\">{lunch_items[i][0]}</td>"
        strRW += f"<td class=\"tg-0lax\">{lunch_items[i][1]}</td>"
        strRW += f"<td class=\"tg-0lax\">{random.choice(Recipe)} {lunch_items[i][1]} with {bf_items[i][0]},<p>{random.choice(Cook)} {bf_items[i][1]}, {lunch_items[i][0]} </p></td></tr>" 
        Html_Str +=strRW

    strTable = strTable+Html_Str+"</table></html>"
    return strTable

bf_items = []
lunch_items = []

for i in range(7):
    bf_item = Breakfast(Fruits, Veggies)
    if len(bf_items)>0:
        if bf_items[i-1][0] == bf_item[0] or bf_items[i-1][1] == bf_item[1]:
            bf_item = Breakfast(Fruits, Veggies)
    bf_items.append(bf_item)

    lunch_item = Lunch(Proteins, Grains)
    if len(lunch_items)>0:
        if lunch_items[i-1][0] == lunch_item[0] or lunch_items[i-1][1] == lunch_item[1]:
            lunch_item = Lunch(Proteins, Grains)
    lunch_items.append(lunch_item)

#################

hs = open("Ridhwaan_Food_Schedule.html", 'w')
hs.write(Html_formater())
