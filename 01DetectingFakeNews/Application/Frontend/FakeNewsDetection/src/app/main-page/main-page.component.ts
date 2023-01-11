import { Component, OnInit } from '@angular/core';
import { FakeNewsDetectionService } from 'src/app/main-page/api/fake-news-detector.service';

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.scss']
})
export class MainPageComponent implements OnInit {

  news: string = "blabla";

  constructor(private fakeNewsDetectionService: FakeNewsDetectionService ) { }

  ngOnInit(): void {
  }

  predict(): void {
    this.fakeNewsDetectionService.postNews(this.news);
    console.log("predict");
  }

}
