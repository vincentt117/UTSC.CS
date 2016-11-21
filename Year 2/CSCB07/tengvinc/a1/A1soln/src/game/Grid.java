package game;

/**
 * A class that represents the generic grid of the vacuum game.
 */
public abstract class Grid<T> {
  /**
   * Returns a T representation of the row and column the calling element
   * resides in.
   * 
   * @param row
   *          the row the element resides in
   * @param column
   *          the column the element resides in
   * @return T representation of the cell
   */
  public abstract T getCell(int row, int column);

  /**
   * Switches the coordinate of T item.
   * 
   * @param row
   *          the row which the element will be switched to
   * @param column
   *          the row which the element will be switched to
   * @param item
   *          the item to have its coordinate switched
   */

  public abstract void setCell(int row, int column, T item);

  /**
   * Returns the number of rows occupied.
   * 
   * @return the number of rows occupied
   */
  public abstract int getNumRows();

  /**
   * Returns the number of columns occupied.
   * 
   * @return the number of columns occupied
   */
  public abstract int getNumColumns();

  @Override
  public abstract int hashCode();

  @Override
  public String toString() {
    String retString = "";
    for (int row = 0; row < this.getNumRows(); row++) {
      for (int col = 0; col < this.getNumColumns(); col++) {
        retString += this.getCell(row, col).toString();
      }
      retString += "\n";

    }
    return retString;
  }

  @SuppressWarnings("unchecked")
  @Override
  public boolean equals(Object obj) {
    // Two grids are equal if they have the same number of rows and grid
    // content
    boolean isEqual = true;
    if (this == obj) {
      return true;
    }
    if (!super.equals(obj)) {
      return false;
    }
    if (getClass() != obj.getClass()) {
      return false;
    }
    if (this.getNumRows() != ((Grid<T>) obj).getNumRows()) {
      return false;
    }
    if (this.getNumRows() != ((Grid<T>) obj).getNumColumns()) {
      return false;
    }
    for (int row = 0; row < this.getNumRows(); row++) {
      for (int col = 0; col < this.getNumColumns(); col++) {
        if (!this.getCell(row, col).equals(((Grid<T>) obj).getCell(row, col))) {
          isEqual = false;
        }
      }

    }
    return isEqual;
  }

}
