import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;

public class druga {
    public static void main(String[] args) throws FileNotFoundException, FileNotFoundException, IOException {
        BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
        Queue<String> vrsta = new LinkedList<String>();
        for (int i = 0; i < 3; i++) 
            vrsta.add(reader.readLine());
        String trenutna = null;
        int counter = 0;
        while ((trenutna = reader.readLine()) != null) {
            vrsta.add(trenutna.trim());
            String prejsna = vrsta.remove();
            if (Integer.valueOf(prejsna) < Integer.valueOf(trenutna)) 
                counter++;
            
        }
        reader.close();
        System.out.println(counter);
    }
}