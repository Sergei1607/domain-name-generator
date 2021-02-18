let pronoun = ['the','our'];
let adj = ['great', 'big' ];
let noun = ['jogger','racoon'];
let sub = [".com", ".net"]
let randoms = []

for (i in pronoun){
    for (j in adj){
        for (k in noun){
            for (l in sub){
                 randoms.push(pronoun[i]+adj[j]+noun[k]+sub[l])
            }
        }
    }
}
console.log(randoms)
document.getElementById("domain").innerHTML= randoms.join('<br>')

