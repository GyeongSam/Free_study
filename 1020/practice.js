
let ans1='*';
for (let n=4;n>=0;--n){
  let ans2='';
  for (let q=0;q<n;++q){
    ans2+=' ';
  }
  console.log(ans2+ans1)
  ans1+='**';
}
