import { Component, OnInit } from '@angular/core';
import {ActivatedRoute,Router} from '@angular/router'
import { CakeService } from '../service/cake.service';
import {FormGroup,FormControl} from '@angular/forms';
import { tap } from 'rxjs/operators';



@Component({
  selector: 'app-productdetail',
  templateUrl: './productdetail.component.html',
  styleUrls: ['./productdetail.component.css']
})
export class ProductdetailComponent implements OnInit{
  id:any
  cake:any
  cakeImages: string[] = [];

  reviewForm=new FormGroup({
    comment:new FormControl(),
    rating:new FormControl() 
  })

  quantityForm=new FormGroup({
  quantity:new FormControl(),
    
  })



  addReview(){
    let formData=this.reviewForm.value
    this.service.addReview(this.id,formData).subscribe(res=>this.ngOnInit())
    
  }

  constructor(private route:ActivatedRoute,private service:CakeService,private router:Router){
   this.id=this.route.snapshot.params['id']
   console.log(this.id)
   
    
  }
  
  ngOnInit(): void {
    this.id = this.route.snapshot.params['id'];
    this.service.getCakeDetail(this.id).pipe(
      tap((res: any) => {
        this.cake = res;
        this.cakeImages = this.cake.images.map((image: any) => image.url);
      })
    ).subscribe();
  }
  

  cartAdd(){
    let formData=this.quantityForm.value
    this.service.addToCart(this.id,formData).subscribe(res=>
    this.router.navigateByUrl("products"))
  }

}
