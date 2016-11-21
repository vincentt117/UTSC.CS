package sprites;

/**
 * A class that represents the basic sprite of the vacuum game.
 */
public abstract class Sprite {
  private char symbol; // Symbol to be displayed in the GUI representing a
  // sprite
  private int row; // The row in which the sprite resides in
  private int column; // The column in which the sprite resides in

  /**
   * Creates a new <code>Sprite</code> that represents a sprite in the game.
   * 
   * @param symbol
   *          the symbol depicting this <code>Sprite</code>
   * @param row
   *          the row which this <code>Sprite</code> resides in now
   * @param column
   *          the column which this <code>Sprite</code> resides in now
   */
  public Sprite(char symbol, int row, int column) {
    this.symbol = symbol;
    this.row = row;
    this.column = column;
  }

  /**
   * Returns the symbol depicting this <code>Sprite</code>.
   * 
   * @return symbol: the symbol depicting this <code>Sprite</code>
   */
  public char getSymbol() {
    return symbol;
  }

  /**
   * Returns the row which this <code>Sprite</code> resides in now.
   * 
   * @return row: the row which this <code>Sprite</code> resides in now
   */
  public int getRow() {
    return row;
  }

  /**
   * Returns the column which this <code>Sprite</code> resides in now.
   * 
   * @return column: the column which this <code>Sprite</code> resides in now
   */
  public int getColumn() {
    return column;
  }

  /**
   * Changes the row and column which this sprite resides in.
   * 
   * @param row:
   *          the new row which this sprite will reside in
   * @param column:
   *          the new column which this sprite will reside in
   */
  protected void updateCoordinates(int row, int column) {
    this.row = row;
    this.column = column;
  }

  @Override
  public int hashCode() {
    final int prime = 31;
    int result = 1;
    result = prime * result + column;
    result = prime * result + row;
    result = prime * result + symbol;
    return result;
  }

  @Override
  public String toString() {
    return "" + this.getSymbol();
  }

  @Override
  public boolean equals(Object obj) {
    if (this == obj) {
      return true;
    }
    if (obj == null) {
      return false;
    }
    if (getClass() != obj.getClass()) {
      return false;
    }
    Sprite other = (Sprite) obj;
    if (column != other.column) {
      return false;
    }
    if (row != other.row) {
      return false;
    }
    if (symbol != other.symbol) {
      return false;
    }
    return true;
  }

}
