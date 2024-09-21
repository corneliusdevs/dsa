// create Node Class
class listNode {
    data = null
    nextNode = null

    constructor(data, nextNode){
        this.data = data
        this.nextNode = nextNode
    }
}

// create Node Objects
const node1 = new listNode(2)
const node2 = new listNode(3)
const node3 = new listNode(4)
const node4 = new listNode(5)

// link the nodes together 
node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4

// loop over the nodes and do some logging
let currentNode = node1

while(currentNode){
    console.log(currentNode.data, " => ")
    currentNode = currentNode.nextNode
}

console.log("end")