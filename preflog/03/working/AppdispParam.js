import React  from 'react'
import axios from 'axios'
export class Disp extends React.Component{
    constructor(){
        super()
        this.state={
            dat:[]
        }
    }						
    componentDidMount(){							
        let dep=prompt('enter dept') 
        axios.get("http://127.0.0.1:4000/fetchrecsparam",
        {params:{dept:dep}}).then(res=>{this.setState({dat:res.data})})
         .catch(err=>console.log(err))
    }
    render()
    {
        var trs=(this.state.dat.length==0) ?<h1>no data</h1>
   :
   this.state.dat.map(e=><tr><td>{e.empno}</td>
   <td>{e.empname}</td>
   <td>{e.dept}</td>
   </tr>)
   return(
       <table border="2.0">
           <th>empnno</th>
           <th>empname</th>
           <th>dept</th>
           <tbody>
               {trs}
           </tbody>
       </table>
   )
    }
}
