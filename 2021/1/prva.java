import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.nio.Buffer;

public class prva {
    public static void main(String[] args) throws FileNotFoundException, FileNotFoundException, IOException {
        BufferedReader reader = new BufferedReader(new FileReader(args[0]));
        String vrstica;
        int prejsna = 0;
        int counter = 0;
        while ((vrstica = reader.readLine()) != null) {
            
            int trenutna = Integer.parseInt(vrstica);
            if (trenutna > prejsna) 
                counter++;
            prejsna = trenutna;
        }
        System.out.println(counter);
    }
}