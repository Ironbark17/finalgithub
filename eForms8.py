
// Import the LinkedHashMap class
import java.util.LinkedHashMap;

public class Main {
  public static void main(String[] args) {
    LinkedHashMap<String, String> capitalCities = new LinkedHashMap<>();

    capitalCities.put("London");
    capitalCities.put("New Dehli");
    capitalCities.put("Wien");
    capitalCities.put( "Oslo");
    capitalCities.put("Norway"); // Duplicate
    capitalCities.put("USA");

    System.out.println(capitalCities);
  }
