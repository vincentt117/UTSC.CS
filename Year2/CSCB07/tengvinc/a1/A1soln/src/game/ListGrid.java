package game;

import java.util.ArrayList;
import java.util.List;

/**
 * A class that represents list representation of the grid of the vacuum game.
 */
public class ListGrid<T> extends Grid<T> {
  private List<List<T>> grid; // A list containing T elements in the grid
  private int numRows; // The number of rows in this grid
  private int numColumns; // The number of columns in this grid

  /**
   * Creates a new list representation.
   * 
   * @param numRows
   *          the number of rows in this grid
   * @param numColumns
   *          the number of column in this grid
   */
  public ListGrid(int numRows, int numColumns) {
    this.numRows = numRows;
    this.numColumns = numColumns;
    this.grid = new ArrayList<List<T>>();
  }

  @Override
  public T getCell(int row, int column) {
    // TODO Auto-generated method stub
    return grid.get(row).get(column);
  }

  @Override
  public void setCell(int row, int column, T item) {
    // TODO Auto-generated method stub
    // Add new list into the grid if the index does not exist
    if (grid.size() <= row) {
      List<T> innerList = new ArrayList<T>();
      innerList.add(column, item);
      grid.add(row, innerList);
    } else {
      if (grid.get(row).size() <= column) {
        grid.get(row).add(column, item);
      } else {
        grid.get(row).set(column, item);
      }
    }

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
