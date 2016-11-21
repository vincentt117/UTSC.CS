package game;

/** Constants used by the VacuumGame. */
public class Constants {

  // ----- constants for game play -----
  enum GridType {
    MAP_GRID, LIST_GRID;
  }

  enum UiType {
    TEXT, GUI;
  }

  // set the following constants:
  public static final String FILENAME = "/cmshome/tengvinc/tengvinc/a1/grid2.txt"; // set
  // to
  // input
  // path
  public static final UiType UI_TYPE = UiType.TEXT; // set to a UiType
  public static final GridType GRID_TYPE = GridType.LIST_GRID; // set a
  // GridType

  // ----- constants that represent grid contents -----

  /** The symbol for a clean location. */
  public static final char CLEAN = ' ';

  /** The symbol for a wall. */
  public static final char WALL = 'X';

  /** The symbol for Player 1. */
  public static final char P1 = '1';

  /** The symbol for Player 2. */
  public static final char P2 = '2';

  /** The symbol for dirt. */
  public static final char DUST = '.';

  /** The symbol for a dust ball. */
  public static final char DUST_BALL = 'o';

  /** The symbol for a dumpster. */
  public static final char DUMPSTER = 'U';

  // ----- constants that relate to scores -----

  /** The initial score. */
  public static final int INIT_SCORE = 0;

  /** The score for cleaning dirt. */
  public static final int DUST_SCORE = 1;

  /** The score for cleaning a dust ball. */
  public static final int DUST_BALL_SCORE = 2;

  /** The capacity for a vacuum. */
  public static final int CAPACITY = 5;

  /** The contents of an empty vacuum. */
  public static final int EMPTY = 0;

  /** The increment of "fullness" for a vacuum. */
  public static final int FULLNESS_INC = 1;

  // ----- constants that represent moves -----

  /** The symbol for Player 1 moving left. */
  public static final char P1_LEFT = 'a';

  /** The symbol for Player 1 moving down. */
  public static final char P1_DOWN = 's';

  /** The symbol for Player 1 moving right. */
  public static final char P1_RIGHT = 'd';

  /** The symbol for Player 1 moving up. */
  public static final char P1_UP = 'w';

  /** The symbol for Player 2 moving left. */
  public static final char P2_LEFT = 'j';

  /** The symbol for Player 2 moving down. */
  public static final char P2_DOWN = 'k';

  /** The symbol for Player 2 moving right. */
  public static final char P2_RIGHT = 'l';

  /** The symbol for Player 2 moving up. */
  public static final char P2_UP = 'i';

  /** The adjustment for moving left. */
  public static final int LEFT = -1;

  /** The adjustment for moving down. */
  public static final int DOWN = 1;

  /** The adjustment for moving right. */
  public static final int RIGHT = 1;

  /** The adjustment for moving up. */
  public static final int UP = -1;

  // ----- in case of a tie -----
  public static char TIE = 'T';
}
