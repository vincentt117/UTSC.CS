package example;

import java.util.Arrays;
import java.util.List;
import java.util.NoSuchElementException;

/**
 * @author anya
 * An example implementation for your tester.
 */
public class SimpleSearch {

  /**
   * Returns the index of the first occurrence of element in list.
   * @param list the list, in which we search for element
   * @param element the element we are searching for in list
   * @return the index of the first occurrence of element in list
   * @throws NoSuchElementException if element does not occur in list
   */
  public static <E> int search(List<E> list, E element) throws NoSuchElementException {
    E elt;
    for (int index = 0; index < list.size(); index ++) {
      elt = list.get(index);
      if (elt.equals(element)) {
        return index;
      }
    }
    throw new NoSuchElementException(String.format("Element %s does not occur in %s", element, list));
  }
  
  /**
   * Provides an example of using the search method.
   * @param args the usual
   */
  public static void main(String[] args) {
    List<String> list = Arrays.asList(new String[] {"hi"});
    System.out.println(search(list, "hi"));
  }
}