import java.util.*;
import java.io.*;
// i will solve this problem with a simple dictionary memorization thing. for each char, there is a set of buttons that must be pushed, it works.
public class T9SpellingSolver {
  public static void main(String[] args) throws IOException {
    // parse

    File inputFile = new File("C-large-practice.in");
    Scanner scan = new Scanner(inputFile);
    ArrayList<String> lines = new ArrayList<String>();
    String outfilename = "output.txt";
    BufferedWriter out = new BufferedWriter(new FileWriter(outfilename));
    // fill lines list
    while (scan.hasNextLine()) {
      lines.add(scan.nextLine());
    }
    String[] key = {"2", "22", "222", "3", "33", "333", "4", "44", "444", "5", "55", "555", "6", "66", "666", "7", "77", "777", "7777", "8", "88", "888", "9", "99", "999", "9999", "0"};
    char[] alph = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '};
    char last = '1';
    for (int i = 1; i < lines.size(); i++) {
      out.write("Case #" + i + ": ");
      char[] line = lines.get(i).toCharArray();
      for (char c : line) {
        if (last == key[getIndex(alph, c)].toCharArray()[0]) {
          out.write(" ");
          last = ' ';
        }
        out.write(key[getIndex(alph, c)]);
        last = key[getIndex(alph, c)].charAt(0);
      }
      out.write("\n");
      last = '1';
    }
    out.close();
    scan.close();
    System.out.println("all done :)");
  }

  public static int getIndex(char[] arr, char c) {
    for (int i = 0; i < arr.length; i++) {
      if (c == arr[i]) {
        return i;
      }
    }
    return -1;
  }

}
