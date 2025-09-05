
import random
import pandas as pd
import matplotlib.pyplot as plt


days=int(input("enter the days:"))

def simple_weather_forecast(location, days):
    conditions = ["Sunny ", "Cloudy", "Rainy", "Stormy", "Windy", "Foggy"]
    forecast_data = []

    for day in range(1, days + 1):
        temperature = random.randint(15, 40)   # °C
        humidity = random.randint(30, 90)      # %

        if humidity > 80 and temperature < 25:
            condition = "Rainy"
        elif temperature > 35:
            condition = "Sunny"
        else:
            condition = random.choice(conditions)

        forecast_data.append([f"Day {day}", location, temperature, humidity, condition])

    # Convert list to DataFrame
    df = pd.DataFrame(forecast_data, columns=["Day", "Location", "Temperature (°C)", "Humidity (%)", "Condition"])
    return df


city = input("Enter your city name: ")
forecast_df = simple_weather_forecast(city, days)

print(f"\n{days}-Day Weather Forecast:\n")
print(forecast_df.to_string(index=False))  # print without index numbers


#  Plot & Save Temperature Graph
plt.figure(figsize=(8,5))
plt.plot(forecast_df["Day"], forecast_df["Temperature (°C)"], marker='o', color="red")
plt.title(f"{days}-Day Temperature Forecast for {city}")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=-90)
plt.grid(True)
temp_graph_file = "temperature_graph.png"
plt.savefig(temp_graph_file)  
plt.show()
print(f"Temperature graph saved as {temp_graph_file}")

#  Plot & Save Humidity Graph
plt.figure(figsize=(8,5))
plt.plot(forecast_df["Day"], forecast_df["Humidity (%)"], marker='s', color="blue")
plt.title(f"{days}-Day Humidity Forecast for {city}")
plt.xlabel("Days")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=-90)
plt.grid(True)
humidity_graph_file = "humidity_graph.png"
plt.savefig(humidity_graph_file)  
plt.show()
print(f"Humidity graph saved as {humidity_graph_file}")




# Save to CSV
forecast_df.to_csv("weather_forecast.csv", index=False)
print("\nForecast saved to weather_forecast.csv")
