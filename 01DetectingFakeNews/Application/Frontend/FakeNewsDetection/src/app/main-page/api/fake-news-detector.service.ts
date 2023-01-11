import { HttpClient } from '@angular/common/http';
import { Injectable} from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class FakeNewsDetectionService {
  private domain: string = environment.serverUrl;

  //TODO: httpClient injection not working yet
  constructor(private http: HttpClient) {}

  postNews(news: string) : Observable<any> {

    return this.http.post(this.domain, news);

  }
}
