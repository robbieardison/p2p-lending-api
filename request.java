import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class BniDisbursementExample {
    public static void main(String[] args) {
        try {
            // BNI API endpoint for disbursement
            String url = "https://api.bni.co.id/disbursement";

            // Your BNI API credentials
            String apiKey = "your_api_key";
            String accessToken = "your_access_token";

            // Disbursement request data
            String requestData = "{"
                    + "\"loan_id\":\"12345\","
                    + "\"borrower_name\":\"John Doe\","
                    + "\"bank_account\":\"1234567890\","
                    + "\"amount\":1000.00"
                    + "}";

            // Create a URL object
            URL obj = new URL(url);

            // Open a connection to the URL
            HttpURLConnection connection = (HttpURLConnection) obj.openConnection();

            // Set the HTTP request method to POST
            connection.setRequestMethod("POST");

            // Set request headers
            connection.setRequestProperty("Api-Key", apiKey);
            connection.setRequestProperty("Authorization", "Bearer " + accessToken);
            connection.setRequestProperty("Content-Type", "application/json");

            // Enable input/output streams
            connection.setDoOutput(true);

            // Write the request data to the output stream
            try (DataOutputStream outputStream = new DataOutputStream(connection.getOutputStream())) {
                outputStream.writeBytes(requestData);
                outputStream.flush();
            }

            // Get the response code
            int responseCode = connection.getResponseCode();

            // Read the response
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String inputLine;
                StringBuilder response = new StringBuilder();

                while ((inputLine = reader.readLine()) != null) {
                    response.append(inputLine);
                }

                // Handle the response
                if (responseCode == 200) {
                    System.out.println("Disbursement request successful");
                    System.out.println("Response: " + response.toString());
                } else {
                    System.out.println("Disbursement request failed");
                    System.out.println("Error: " + response.toString());
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
