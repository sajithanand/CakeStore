import { Component, OnInit } from '@angular/core';
import { CakeService } from '../service/cake.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-orderlist',
  templateUrl: './orderlist.component.html',
  styleUrls: ['./orderlist.component.css']
})
export class OrderlistComponent implements OnInit {
  
  orders:any
  id:any;
  
  constructor(private service:CakeService,public router:Router){

  }
  ngOnInit(): void {
    this.service.listOrder().subscribe(res=>this.orders=res)
    
  }


  cancel(){
    this.service.OrderDelete(this.orders).subscribe(res=>
    this.router.navigateByUrl("products"))
  }



  cancelOrder(orderId: number): void {
    
    if (confirm('Are you sure you want to cancel this order?')) {
      this.service.OrderDelete(orderId).subscribe(
        res => {
          this.router.navigateByUrl("products");
        },
        error => {
          console.error('Error canceling order:', error);
          alert('Failed to cancel order. Please try again.');
        }
      );
    }
  }
  

  

}
