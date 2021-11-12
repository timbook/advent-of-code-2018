import scala.io.Source

val lines = Source.fromFile("../data/12-input.txt").getLines.toArray

var initState = lines(0).split(" ").last
    .zipWithIndex
    .map(t => t._2 -> t._1.toString)
    .toMap

val rules = lines
    .drop(2)
    .map(s => s.split(" => "))
    .map(t => t(0) -> t(1))
    .toMap

def getLayout(n: Int) = ((n - 2) to (n + 2)).map(state.getOrElse(_, ".")).mkString

def simGeneration(state: Map[Int, String]) = {
    val minPot = state.keys.min
    val maxPot = state.keys.max
    
    val stateWider = state ++ List(
        (minPot - 2 -> "."),
        (minPot - 1 -> "."),
        (maxPot + 1 -> "."),
        (maxPot + 2 -> ".")
    )

    stateWider
        .map(t => t._1 -> getLayout(t._1))
        .map(t => t._1 -> rules(t._2))
}

def countPlants(state: Map[Int, String]) = state.map(t => if (t._2 == "#") t._1 else 0).sum

var state = initState
for (i <- 1 to 20) state = simGeneration(state)

println(countPlants(state))
