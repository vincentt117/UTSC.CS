package tests;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import java.io.IOException;
import java.text.ParseException;
import java.util.Arrays;
import java.util.List;
import java.util.NoSuchElementException;

import org.junit.Test;

import example.SimpleSearch;

public class SimpleSearchTest {
  public static final List<String> oneList = Arrays.asList(new String[] { "1" });
  public static final List<String> difList = Arrays.asList(new String[] { "1", "2", "3" });
  public static final List<String> sameList = Arrays.asList(new String[] { "1", "1", "1" });

  public static final int TIMEOUT = 100;

  @Test(timeout = TIMEOUT)
  public void testSearch() throws IOException, ParseException {
    // Test for valid return type
    assertTrue("Did not return integer index",
        SimpleSearch.search(oneList, "1") == (int) SimpleSearch.search(oneList, "1"));

    // Test with only one element
    int actualOne = SimpleSearch.search(oneList, "1");
    int expectOne = 0;
    assertEquals(String.format("Expected: %s, got: %s", expectOne, actualOne), expectOne,
        actualOne);

    // Test with multiple different elements, looking for the first
    int actualDif = SimpleSearch.search(difList, "1");
    int expectDif = 0;
    assertEquals(String.format("Expected: %s, got: %s", expectDif, actualDif), expectDif,
        actualDif);

    // Test with multiple different elements, looking for the first
    int actualDif1 = SimpleSearch.search(difList, "2");
    int expectDif1 = 1;
    assertEquals(String.format("Expected: %s, got: %s", expectDif1, actualDif1), expectDif1,
        actualDif1);

    // Test with multiple different elements, looking for the first
    int actualDif2 = SimpleSearch.search(difList, "3");
    int expectDif2 = 2;
    assertEquals(String.format("Expected: %s, got: %s", expectDif2, actualDif2), expectDif2,
        actualDif2);

    // Test with multiple identical elements
    int actualSame = SimpleSearch.search(sameList, "1");
    int expectSame = 0;
    assertEquals(String.format("Expected: %s, got: %s", expectSame, actualSame), expectSame,
        actualSame);

    try {
      SimpleSearch.search(difList, "x");
      fail("Expected NoSuchElementException");
    } catch (NoSuchElementException ex) {
      return;
    }

  }

}
