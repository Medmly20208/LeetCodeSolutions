/**
 * @param {string} path
 * @return {boolean}
 */
var isPathCrossing = function(path) {
    let current = [0,0];
    let count = [[0,0]]
    let t,k,y;
    let r = [] ;
    for(let i = 0;i<path.length;i++){
        if(path[i]=="N"){
            current[1]+=1
            
        }
        else if(path[i]=="S"){
             current[1]-=1
        }
        else if(path[i]=="W"){
            current[0]-=1
        }
        else{
           current[0]+=1
        }
        k = current[0]
        y = current[1]
        
        t = count.map(function(e){
            if(k === e[0] && y==e[1]){
               r.push(true)     
            }
            else{
                r.push(false)
            }
            
        })
        
        
        if(r.includes(true)){
            return true
        }
        else{
            r.splice(0, r.length);
            count.push([k,y])
        }
        
      
     
    }
    return false
};