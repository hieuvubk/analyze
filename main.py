import pandas as pd
import matplotlib.pyplot as plt


df_teams = pd.read_excel("data_neww.xlsx")
markets = df_teams['Market'].tolist()
value = df_teams['Totals'].tolist()
print(markets, len(markets))
print(value, len(value))
fig = plt.figure(figsize = (40, 8))
plt.bar(markets, value, color ='maroon', 
        width = 0.4)
 
plt.xlabel("Markets")
plt.ylabel("Values")
plt.title("2023 visitor to Vietnam")

current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in current_values])
plt.xticks(rotation=90)

plt.show()
# df_teams_countries_disciplines = df_teams.groupby(by="Market").agg({"Year":'sorted'}).reset_index().sort_values(by='Year', ascending=False)
# print(df_teams_countries_disciplines)
# ax = df_teams_countries_disciplines.plot.bar(x='Market', xlabel = 'Nothing', figsize=(20,8))
