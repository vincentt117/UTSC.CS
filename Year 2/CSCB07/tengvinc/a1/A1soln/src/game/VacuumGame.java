package game;

import game.Constants;
import sprites.CleanHallway;
import sprites.Dirt;
import sprites.Dumpster;
import sprites.Dust;
import sprites.DustBall;
import sprites.Sprite;
import sprites.Vacuum;
import sprites.Wall;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

/**
 * A class that represents the basic functionality of the vacuum game. This
 * class is responsible for performing the following operations: 1. At creation,
 * it initializes the instance variables used to store the current state of the
 * game. 2. When a move is specified, it checks if it is a legal move and makes
 * the move if it is legal. 3. It reports information about the current state of
 * the game when asked.
 */
public class VacuumGame {

  private Random random; // a random number generator to move the DustBalls
  private Grid<Sprite> grid; // the grid
  private Vacuum vacuum1; // the first player
  private Vacuum vacuum2; // the second player
  private List<Dust> dusts; // the dusts
  private List<DustBall> dustBalls; // the dust balls

  /**
   * Creates a new <code>VacuumGame</code> that corresponds to the given input
   * text file. Assumes that the input file has one or more lines of equal
   * lengths, and that each character in it (other than newline) is a character
   * that represents one of the <code>Sprite</code>s in this game. Uses gridType
   * to implement the grid.
   * 
   * @param layoutFileName
   *          path to the input grid file
   * @param gridType
   *          the type of grid implementation to use
   */
  public VacuumGame(String layoutFileName, Constants.GridType gridType) throws IOException {
    dusts = new ArrayList<>();
    dustBalls = new ArrayList<>();
    random = new Random();

    // open the file, read the contents, and determine dimensions of the
    // grid
    int[] dimensions = getDimensions(layoutFileName);
    int numRows = dimensions[0];
    int numColumns = dimensions[1];

    if (gridType.equals(Constants.GridType.LIST_GRID)) {
      grid = new ListGrid<>(numRows, numColumns);
    } else {
      grid = new MapGrid<>(numRows, numColumns);
    }

    // open the file again, read the contents, and store them in grid
    Scanner sc = new Scanner(new File(layoutFileName));
    for (int row = 0; row < numRows; row++) {
      String nextLine = sc.nextLine();

      /********
       * Initialize the grid
       ********/
      // Look through the file and declare Sprites based on the symbol
      for (int col = 0; col < numColumns; col++) {
        if (nextLine.charAt(col) == Constants.CLEAN) {
          grid.setCell(row, col, new CleanHallway(row, col));
        } else if (nextLine.charAt(col) == Constants.DUMPSTER) {
          grid.setCell(row, col, new Dumpster(row, col));
        } else if (nextLine.charAt(col) == Constants.DUST) {
          dusts.add(new Dust(row, col, Constants.DUST_SCORE));
          grid.setCell(row, col, dusts.get(dusts.size() - 1));
        } else if (nextLine.charAt(col) == Constants.DUST_BALL) {
          dustBalls.add(new DustBall(row, col, Constants.DUST_BALL_SCORE));
          grid.setCell(row, col, dustBalls.get(dustBalls.size() - 1));
        } else if (nextLine.charAt(col) == Constants.P1) {
          vacuum1 = new Vacuum(Constants.P1, row, col, Constants.CAPACITY);
          vacuum1.setUnder(new CleanHallway(row, col));
          grid.setCell(row, col, vacuum1);
        } else if (nextLine.charAt(col) == Constants.P2) {
          vacuum2 = new Vacuum(Constants.P2, row, col, Constants.CAPACITY);
          vacuum2.setUnder(new CleanHallway(row, col));
          grid.setCell(row, col, vacuum2);
        } else if (nextLine.charAt(col) == Constants.WALL) {
          grid.setCell(row, col, new Wall(row, col));
        }
      }

    }
    sc.close();
  }

  /*********
   * Lots of methods.
   ************/
  /**
   * Return the number of rows in the grid.
   * 
   * @return the number of rows in the grid
   */
  public int getNumRows() {
    return this.grid.getNumRows();
  }

  /**
   * Return the number of columns in the grid.
   * 
   * @return the number of columns in the grid
   */
  public int getNumColumns() {
    return this.grid.getNumColumns();
  }

  /**
   * Return the <code>Sprite</code> at the parameter coordinate.
   * 
   * @param row
   *          the row to find the <code>Sprite</code>
   * @param col
   *          the column to find the <code>Sprite</code>
   * @return the <code>Sprite</code> at the parameter coordinate
   */
  public Sprite getSprite(int row, int col) {
    return grid.getCell(row, col);
  }

  /**
   * Returns the grid containing the <code>Sprite</code>s of the current game.
   * 
   * @return the grid containing the <code>Sprite</code>s of the current game
   */
  public Grid<Sprite> getGrid() {
    return grid;
  }

  /**
   * Return <code>Vacuum</code> vacuum1.
   * 
   * @return vacuum1
   */
  public Vacuum getVacuumOne() {
    return vacuum1;
  }

  /**
   * Return <code>Vacuum</code> vacuum2.
   * 
   * @return vacuum2
   */
  public Vacuum getVacuumTwo() {
    return vacuum2;
  }

  /**
   * Move the appropriate <code>Vacuum</code> based on the command nextMove
   * depending on whether the move is legal.
   * 
   * @param nextMove
   *          the key passed in which will determine the next move in the game
   */
  public void move(char nextMove) {
    if (nextMove == Constants.P1_LEFT) {
      this.physicalMove(vacuum1, 0, Constants.LEFT);
    } else if (nextMove == Constants.P1_DOWN) {
      this.physicalMove(vacuum1, Constants.DOWN, 0);
    } else if (nextMove == Constants.P1_RIGHT) {
      this.physicalMove(vacuum1, 0, Constants.RIGHT);
    } else if (nextMove == Constants.P1_UP) {
      this.physicalMove(vacuum1, Constants.UP, 0);
    } else if (nextMove == Constants.P2_LEFT) {
      this.physicalMove(vacuum2, 0, Constants.LEFT);
    } else if (nextMove == Constants.P2_DOWN) {
      this.physicalMove(vacuum2, Constants.DOWN, 0);
    } else if (nextMove == Constants.P2_RIGHT) {
      this.physicalMove(vacuum2, 0, Constants.RIGHT);
    } else if (nextMove == Constants.P2_UP) {
      this.physicalMove(vacuum2, Constants.UP, 0);
    }

  }

  /**
   * Attempt to move the Vacuum vacToMove based on the passed in specifications.
   * If the move was legal, move the dust balls and perform any necessary
   * actions based on the move made by the vacuum (clean, empty, etc,..)
   * 
   * @param vacToMove:
   *          The vacuum to be moved
   * @param rowMod:
   *          the change in row
   * @param colMod:
   *          the change in column
   */
  private void physicalMove(Vacuum vacToMove, int rowMod, int colMod) {

    // If the move is legal based on the specifications, perform it
    if (!(grid.getCell(vacToMove.getRow() + rowMod, vacToMove.getColumn() + colMod) instanceof Wall)
        && !(grid.getCell(vacToMove.getRow() + rowMod,
            vacToMove.getColumn() + colMod) instanceof Vacuum)) {
      int moveDir = 0;
      boolean cleansed = true;
      // Take what used to be under the vacuum and return it to where it
      // was
      grid.setCell(vacToMove.getRow(), vacToMove.getColumn(), vacToMove.getUnder());
      // Set what was located at the coordinate to be moved to to be under
      // the moving vacuum
      vacToMove.setUnder(grid.getCell(vacToMove.getRow() + rowMod, vacToMove.getColumn() + colMod));
      vacToMove.moveTo(vacToMove.getRow() + rowMod, vacToMove.getColumn() + colMod);
      grid.setCell(vacToMove.getRow(), vacToMove.getColumn(), vacToMove);
      // If the cleanse is successful, place a clean hallway under the
      // vacuum else the dirt remains under it
      if (vacToMove.getUnder() instanceof Dust) {
        cleansed = vacToMove.clean(Constants.DUST_SCORE);
      } else if (vacToMove.getUnder() instanceof DustBall) {
        cleansed = vacToMove.clean(Constants.DUST_BALL_SCORE);
      }
      if (vacToMove.getUnder() instanceof Dumpster) {
        vacToMove.empty();
      } else if (cleansed) {
        vacToMove.setUnder(new CleanHallway(vacToMove.getRow(), vacToMove.getColumn()));
      }
      // Move all dustballs randomly
      for (int row = 0; row < getNumRows(); row++) {
        // 0 being left, 1 being down, 2, being right, and 3 being up
        for (int col = 0; col < getNumColumns(); col++) {
          if (grid.getCell(row, col) instanceof DustBall) {
            moveDir = this.random.nextInt(4);
            this.moveDustBalls((DustBall) grid.getCell(row, col), moveDir);
          }
        }
      }

    }
  }

  /**
   * Move all <code>DustBall</code> in the game.
   */
  private void moveDustBalls(DustBall db, int moveDir) {
    // Move DustBall db if it ends up moving on top of a CleanHallway or
    // dust
    if (moveDir == 0
        && (grid.getCell(db.getRow(), db.getColumn() - 1) instanceof CleanHallway
            || grid.getCell(db.getRow(), db.getColumn() - 1) instanceof Dust)
        && !(grid.getCell(db.getRow(), db.getColumn() - 1) instanceof DustBall)) {
      this.leaveDust(db);
      db.moveTo(db.getRow(), db.getColumn() - 1);
      grid.setCell(db.getRow(), db.getColumn(), db);
    } else if (moveDir == 1
        && (grid.getCell(db.getRow() - 1, db.getColumn()) instanceof CleanHallway
            || grid.getCell(db.getRow() - 1, db.getColumn()) instanceof Dust)
        && !(grid.getCell(db.getRow() - 1, db.getColumn()) instanceof DustBall)) {
      this.leaveDust(db);
      db.moveTo(db.getRow() - 1, db.getColumn());
      grid.setCell(db.getRow(), db.getColumn(), db);
    } else if (moveDir == 2
        && (grid.getCell(db.getRow(), db.getColumn() + 1) instanceof CleanHallway
            || grid.getCell(db.getRow(), db.getColumn() + 1) instanceof Dust)
        && !(grid.getCell(db.getRow(), db.getColumn() + 1) instanceof DustBall)) {
      this.leaveDust(db);
      db.moveTo(db.getRow(), db.getColumn() + 1);
      grid.setCell(db.getRow(), db.getColumn(), db);
    } else if (moveDir == 3
        && (grid.getCell(db.getRow() + 1, db.getColumn()) instanceof CleanHallway
            || grid.getCell(db.getRow() + 1, db.getColumn()) instanceof Dust)
        && !(grid.getCell(db.getRow() + 1, db.getColumn()) instanceof DustBall)) {
      this.leaveDust(db);
      db.moveTo(db.getRow() + 1, db.getColumn());
      grid.setCell(db.getRow(), db.getColumn(), db);
    }
  }

  /**
   * Leave a Dust in the cell occupied by the DustBall.
   * 
   * @param db
   *          the DustBall that is moving
   */
  private void leaveDust(DustBall db) {
    Boolean noOldDust = true;
    // Leave a dust in the cell that was previously occupied by the
    // DustBall, assuming there was not one there previously
    // Loop through the collection of Dust in VacuumGame and if one holds
    // the same coordinate as the DustBall db place it where db is
    for (int i = 0; i < dusts.size(); i++) {
      if (dusts.get(i).getRow() == db.getRow() && dusts.get(i).getColumn() == db.getColumn()) {
        grid.setCell(db.getRow(), db.getColumn(), dusts.get(i));
        noOldDust = false;
      }
    }
    if (noOldDust) {
      Dust newDust = new Dust(db.getRow(), db.getColumn(), Constants.DUST_SCORE);
      dusts.add(newDust);
      grid.setCell(db.getRow(), db.getColumn(), newDust);
    }
  }

  /**
   * Check whether or not there remains any <code>Dust</code> or
   * <code>DustBall</code> in the grid. Return this fact as whether or not the
   * game is over.
   * 
   * @return isOver: whether or not the game is over
   */
  public boolean gameOver() {
    boolean isOver = true;
    for (int row = 0; row < this.getNumRows(); row++) {
      for (int col = 0; col < this.getNumColumns(); col++) {
        if (this.grid.getCell(row, col) instanceof Dirt) {
          isOver = false;

        }
      }
    }
    return isOver;
  }

  /**
   * Returns the winner of the game. Return tie if the result is a tie
   * 
   * @return The symbol representing the winner of the game or string
   *         representing a tie
   */
  public char getWinner() {
    // determine winner
    if (vacuum1.getScore() > vacuum2.getScore()) {
      return Constants.P1;
    } else if (vacuum1.getScore() < vacuum2.getScore()) {
      return Constants.P2;
    } else {
      return Constants.TIE;
    }
  }

  public String displayGame() {
    return grid.toString();
  }

  /**
   * Returns the dimensions of the grid in the file named layoutFileName.
   * 
   * @param layoutFileName
   *          path of the input grid file
   * @return an array [numRows, numCols], where numRows is the number of rows
   *         and numCols is the number of columns in the grid that corresponds
   *         to the given input grid file
   * @throws IOException
   *           if cannot open file layoutFileName
   */
  private int[] getDimensions(String layoutFileName) throws IOException {

    Scanner sc = new Scanner(new File(layoutFileName));

    // find the number of columns
    String nextLine = sc.nextLine();
    int numCols = nextLine.length();

    // find the number of rows
    int numRows = 1;
    while (sc.hasNext()) {
      numRows++;
      nextLine = sc.nextLine();
    }

    sc.close();
    return new int[] { numRows, numCols };
  }
}
