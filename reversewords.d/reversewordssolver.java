import java.util.*;
import java.io.*;

public class ReverseWordsSolver {
  public static void main(String[] args) throws IOException{
    // parse file
    File file = new File("B-large-practice.in");
    Scanner reader = new Scanner(file);
    ArrayList<String> lines = new ArrayList<String>();
    while (reader.hasNext()) {
      lines.add(reader.nextLine());
    }
    // now we have an array of all the lines (strings)
    for (int casenum = 1; casenum < lines.size(); casenum++) {
      String[] words = lines.get(casenum).split(" ", -1);
      // now words  is a list of each case's words.

      String[] revwords = new String[words.length];
      for (int i = 0; i < words.length; i++) {
        revwords[i] = words[words.length - i - 1];
      }
      String ans = "";
      for (String value : revwords) {
        ans = ans + value + " ";
      }
      ans.trim();
      System.out.println("Case #" + casenum + ": " + ans);
    }
  }
}
