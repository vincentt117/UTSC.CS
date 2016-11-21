package game;

import java.util.HashMap;
import java.util.Map;

/**
 * A class that represents list representation of the grid of the vacuum game.
 */
public class MapGrid<T> extends Grid<T> {
  private Map<Integer, Map<Integer, T>> grid; // A list containing T elements
  // in the grid
  private int numRows; // The number of rows in this grid
  private int numColumns; // The number of columns in this grid

  /**
   * Creates a new list representation.
   * 
   * @param numRows
   *          numRows the number of rows in this grid
   * @param numColumns
   *          the number of column in this grid
   */
  public MapGrid(int numRows, int numColumns) {
    this.numRows = numRows;
    this.numColumns = numColumns;
    this.grid = new HashMap<Integer, Map<Integer, T>>();
  }

  @Override
  public T getCell(int row, int column) {
    // TODO Auto-generated method stub
    return grid.get(row).get(column);
  }

  @Override
  public void setCell(int row, int column, T item) {
    // TODO Auto-generated method stub

    if (grid.get(row) == null) {
      HashMap<Integer, T> innerMap = new HashMap<Integer, T>();
      innerMap.put(column, item);
      grid.put(row, innerMap);
    }
    grid.get(row).put(column, item);

  }

  @Override
  public int getNumRows() {
    // TODO Auto-generated method stub
    return numRows;
  }

  @Override
  public int getNumColumns() {
    // TODO Auto-generated method stub
    return numColumns;
  }

  @Override
  public int hashCode() {
    final int prime = 31;
    int result = 1;
    result = prime * result + ((grid == null) ? 0 : grid.hashCode());
    result = prime * result + numColumns;
    result = prime * result + numRows;
    return result;
  }

}
