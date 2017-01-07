
var yourself = {
    fibonacci : function(n) {
        
        if (n === 0 || n === 1 ) {
            return n;
        }
        
        else {
             var before=0;
             var prev=1;
             var present=1;
            for(var i=1; i<n; i++)
            {  
                present=prev+before;
                before=prev 
                prev=present;
               
               
            }
            return present;   
            }
            
        }
};
