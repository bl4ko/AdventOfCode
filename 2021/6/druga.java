import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.util.ArrayList;

public class druga {
    public static void main(String[] args) throws IOException{
        BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
        String[] zacetek = reader.readLine().strip().split(",");
        ArrayList<Integer> zacetek2 = new ArrayList<>();
        for (int i = 0; i < zacetek.length; i++)
            zacetek2.add(Integer.parseInt(zacetek[i]));
        
        for (int j = 0; j < 256; j++) {
            for (int k = 0; k < zacetek2.size(); k++) {

            }

        }
        
    }
}