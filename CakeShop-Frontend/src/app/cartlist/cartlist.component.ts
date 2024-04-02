import { Component, OnInit } from '@angular/core';
import { CakeService } from '../service/cake.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-cartlist',
  templateUrl: './cartlist.component.html',
  styleUrls: ['./cartlist.component.css']
})
export class CartlistComponent implements OnInit{
  carts:any

  price:any;

  

  // index:any;

  


deleteCartItem(cartItemId: any): void {
    
  if (confirm('Are you sure you want to cancel this order?')) {
    this.service.cartDelete(cartItemId).subscribe(
      res => {
        this.router.navigateByUrl("cartlist");
      },
      error => {
        console.error('Error canceling order:', error);
        alert('Failed to cancel order. Please try again.');
      }
    );
  }
}




  


  




  constructor(private service:CakeService,public router:Router,private route:ActivatedRoute){
  

  }
  
  ngOnInit(): void {
    this.service.listCart().subscribe(res=>this.carts=res
    ),
    
    this.service.getTotalPrice().subscribe(res=>this.price=res
      )

     
  }

}
