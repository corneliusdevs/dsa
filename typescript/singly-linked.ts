
// create Node class
class NodeClass {
    // define class variables
    data:any;
    nextNode:NodeClass | null

   constructor(data:any, nextNode:NodeClass | null = null){
    this.data = data
    this.nextNode = nextNode
   }

}

// create nodes
const node1 = new NodeClass(3)
const node2 = new NodeClass(4)
const node3 = new NodeClass(5)
const node4 = new NodeClass(6)

// link nodes
node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4

let currentNode: NodeClass | null = node1

while (currentNode){
    console.log(currentNode.data, " => ")
    currentNode = currentNode.nextNode
}

console.log("end")